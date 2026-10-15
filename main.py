from datetime import datetime

def convertFromFormat1(jsonObject):
    parts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": parts[0],
            "city": parts[1],
            "area": parts[2],
            "factory": parts[3],
            "section": parts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


def convertFromFormat2(jsonObject):
    date = datetime.fromisoformat(
        jsonObject["timestamp"].replace("Z", "+00:00")
    )
    milliseconds = int(date.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": milliseconds,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }


import json

with open("data-1.json", "r", encoding="utf-8") as file:
    data1 = json.load(file)

with open("data-2.json", "r", encoding="utf-8") as file:
    data2 = json.load(file)

result1 = convertFromFormat1(data1)
result2 = convertFromFormat2(data2)

print("Format 1 result:")
print(json.dumps(result1, indent=4))

print("Format 2 result:")
print(json.dumps(result2, indent=4))


with open("data-result.json", "r", encoding="utf-8") as file:
    expected = json.load(file)

print("Format 1 matches expected:", result1 == expected)
print("Format 2 matches expected:", result2 == expected)

