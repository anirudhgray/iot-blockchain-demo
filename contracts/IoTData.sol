// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IoTData {
    struct SensorData {
        uint256 deviceId;
        uint256 temperature;
        uint256 humidity;
        uint256 timestamp;
    }

    // Array to store sensor data
    SensorData[] public sensorDataRecords;

    // Event to trigger an alert when critical temperature is detected
    event CriticalTemperatureAlert(
        uint256 deviceId,
        uint256 temperature,
        uint256 timestamp
    );

    // Critical temperature threshold (can be set to any value)
    uint256 public criticalTemperature = 40;

    // Function to store IoT data
    function storeData(
        uint256 _deviceId,
        uint256 _temperature,
        uint256 _humidity
    ) public {
        // Store the IoT data in the array
        SensorData memory newData = SensorData({
            deviceId: _deviceId,
            temperature: _temperature,
            humidity: _humidity,
            timestamp: block.timestamp
        });
        sensorDataRecords.push(newData);

        // Check if the temperature exceeds the critical threshold
        if (_temperature > criticalTemperature) {
            // Trigger the event for critical temperature
            emit CriticalTemperatureAlert(
                _deviceId,
                _temperature,
                block.timestamp
            );
        }
    }

    // Function to get the number of stored records
    function getDataCount() public view returns (uint256) {
        return sensorDataRecords.length;
    }

    // Function to retrieve data by index
    function getData(
        uint256 index
    ) public view returns (uint256, uint256, uint256, uint256) {
        SensorData memory data = sensorDataRecords[index];
        return (data.deviceId, data.temperature, data.humidity, data.timestamp);
    }
}
