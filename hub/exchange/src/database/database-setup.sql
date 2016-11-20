
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

CREATE TABLE IF NOT EXISTS "Request" (
	"id" PRIMARY KEY,
	"timestamp" DATETIME DEFAULT current_timestamp,
	"sender" TEXT,
	"receiver" TEXT,
	"action" TEXT,
	"value" TEXT
);

CREATE TABLE IF NOT EXISTS "Event" (
	"id" PRIMARY KEY,
	"timestamp" DATETIME DEFAULT current_timestamp,
	"request_id" INTEGER,
	"sender" TEXT,	
	"attribute" TEXT,
	"value" TEXT
);

CREATE TABLE IF NOT EXISTS "Device" (
	"id" PRIMARY KEY,
	"type" INTEGER,
	"name" TEXT,
	"address" TEXT,
	FOREIGN KEY("type") REFERENCES "event"("id")
);

CREATE TABLE IF NOT EXISTS "Device_Type" (
	"id" PRIMARY KEY,
	"name" TEXT,
	"protocol" INTEGER,
	"input" INTEGER,
	"maker" TEXT,
	"version" TEXT
);
