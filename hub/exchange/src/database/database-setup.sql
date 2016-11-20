/*
id        --  auto incrementing integer key
timestamp --  date and time of the request
source    --  UUID of the sending device
receiver  --  UUID of the receiving device
action    --  what attribute is being changed
value     --  what to change a device value to 
*/
CREATE TABLE IF NOT EXISTS "Request" (
	"id" PRIMARY KEY,
	"timestamp" DATETIME DEFAULT current_timestamp,
	"source" TEXT,
	"receiver" TEXT,
	"action" TEXT,
	"value" TEXT
);

/*
id          --  auto incrementing integer key
timestamp   --  date and time of the request
request_id  --  id of the request in the Request table that caused this event
source      --  UUID of the sending device
attribute   --  what is being changed (ex brightness, hue, etc)
value       --  what to set the attribute to 
*/
CREATE TABLE IF NOT EXISTS "Event" (
	"id" PRIMARY KEY,
	"timestamp" DATETIME DEFAULT current_timestamp,
	"request_id" INTEGER,
	"source" TEXT,	
	"attribute" TEXT,
	"value" TEXT
);

/*
id        --  auto incrementing integer key
protocol  --  specifies what adapter will be needed (Z-Wave, WeMo, etc)
type      --  0 = sensor   1 = device
name      --  user specified name of the device
address   --  UUID of the device or sensor 
*/
CREATE TABLE IF NOT EXISTS "Device" (
	"id" PRIMARY KEY,
	"protocol" INTEGER,
	"type" INTEGER,
	"name" TEXT,
	"address" TEXT,
	FOREIGN KEY("type") REFERENCES "event"("id")
);

/*
This is all getting changed most likely 


id        --  auto incrementing integer key
name      --  user specified name of the device
protocol  --  specifies what adapter will be needed (Z-Wave, WeMo, etc)
input     --  something 
maker     --  device company (Samsung, Aeon Labd, etc)
version   --  firmware version of device
*/
CREATE TABLE IF NOT EXISTS "Device_Type" (
	"id" PRIMARY KEY,
	"name" TEXT,
	"protocol" INTEGER,
	"input" INTEGER,
	"maker" TEXT,
	"version" TEXT
);
