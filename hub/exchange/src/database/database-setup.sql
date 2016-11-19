
CREATE TABLE IF NOT EXISTS "User" (
	"id" PRIMARY KEY,
	"firstname" TEXT,
	"lastname" TEXT,
	"username" TEXT,
	"password" TEXT
);

CREATE TABLE IF NOT EXISTS "UserDevices" (
	"userid" INTEGER,
	"deviceid" INTEGER,
	FOREIGN KEY("userid") REFERENCES "User"("id"),
	FOREIGN KEY("deviceid") REFERENCES "Device"("id")
);

CREATE TABLE IF NOT EXISTS "Event" (
	"id" PRIMARY KEY,
	"type" INTEGER,
	"sender" INTEGER,
	"receiver" INTEGER,
	"timestamp" DATETIME DEFAULT current_timestamp,
	"key" TEXT,
	"value" TEXT
);

CREATE TABLE IF NOT EXISTS "Device" (
	"type" TEXT,
	"name" TEXT,
	"address" TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS "Device_Type" (
	"id" PRIMARY KEY,
	"name" TEXT,
	"protocol" INTEGER,
	"input" INTEGER,
	"maker" TEXT,
	"version" TEXT
);
