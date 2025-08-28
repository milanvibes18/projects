-- devices table (optional)
CREATE TABLE devices (
    device_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT
);

-- sensors table
CREATE TABLE sensors (
    sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id INTEGER,
    type TEXT NOT NULL,
    unit TEXT NOT NULL,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

-- readings table
CREATE TABLE readings (
    reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER,
    value REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sensor_id) REFERENCES sensors(sensor_id)
);
