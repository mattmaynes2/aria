/*
id        --  auto incrementing integer key
timestamp --  date and time of the request
source    --  UUID of the sending device
receiver  --  UUID of the receiving device
attribute --  what attribute is being changed
value     --  what to change a device value to 
*/
CREATE TABLE IF NOT EXISTS "Request" (
	"id" PRIMARY KEY,
	"timestamp" DATETIME DEFAULT current_timestamp,
	"source" TEXT,
	"receiver" TEXT,
	"attribute" TEXT,
	"value" TEXT
);

/*
id          --  auto incrementing integer key
timestamp   --  date and time of the request
request_id  --  id of request in Request table which caused the event, 0 if not caused by request
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
id          --  auto incrementing integer key
name        --  user specified name of the device
protocol    --  specifies what adapter will be needed (Z-Wave, WeMo, etc)
is_input    --  0 = not  1 = yes
maker       --  device company (Samsung, Aeon Labd, etc)
*/
CREATE TABLE IF NOT EXISTS "Device_Type" (
	"id" PRIMARY KEY,
	"name" TEXT,
	"protocol" INTEGER,
	"is_input" INTEGER,
	"maker" TEXT
);

/*
address   --  UUID of device or sensor
version   --  firmware version of device 
type      --  user specified name of device
*/
CREATE TABLE IF NOT EXISTS "Device" (
	"address" TEXT PRIMARY KEY ,
	"version" TEXT,
	"type" INTEGER,
	FOREIGN KEY("type") REFERENCES "Device_Type"("id")
);

/*
id         --  auto incrementing integer key
name       --  name of the attribute
data_type  --  the type of data returned when an attribute is performed
*/
CREATE TABLE IF NOT EXISTS "Attributes" (
	"id" PRIMARY KEY,
	"name" TEXT,
	"data_type" TEXT,
);

/*
attribute_id --  an id linking to an id in the Attributes table
data_type    --  the type of data returned when an attribute is performed
max          --  maximum value of an Integer value
min          --  minimum value of an Integer value
step         --  the increment or decrement value
*/
CREATE TABLE IF NOT EXISTS "Parameter" {
	"attribute_id" INTEGER,
	"data_type" TEXT,
	"max" INTEGER,
	"min" INTEGER,
	"step" INTEGER,
	FOREIGN KEY ("attribute_id") REFERENCES "Attributes"("id")
}

/*
device_type_id  --  an id linking to an id in the Device table
attribute_id    --  an id linking to an id in the Attributes table 
*/
CREATE TABLE IF NOT EXISTS "Device_Type_Attributes" (
	"device_type_id" INTEGER,
	"attribute_id" INTEGER,
	FOREIGN KEY("device_type_id") REFERENCES "Device_Type"("id"),
	FOREIGN KEY("attribute_id") REFERENCES "Atributes"("id")
);



