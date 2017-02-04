### Training REST API

#### GET /behaviour {-}

*Parameters*
start : Start is a Behaviour ID
count : Number of records to return

*Response Format*
{																	
"records": [{
			id: < integer > ,
			name: < string > ,
			createdDate: < datetime > ,
			lastUpdated: < datetime > ,
			active: < boolean >
	}
	...
]														
}			

#### POST /behaviour {-}

*Parameters*
name: String name to identify the behaviour

*Response Format*
{
    "id" : < integer >
}

#### DELETE /behaviour {-}

*Parameters*
id: The integer ID of the behaviour to delete

*Response Format*
200 OK

#### POST /behaviour {-}

*Parameters*
id: The integer id of the behaviour to edit

*Response*
200 OK

#### GET /session {-}

*Parameters*
start : Start is a Session ID
count : Number of records to return

*Response Format*
{																	
"records": [{
			id: < integer > ,
            behaviourId : < integer >,
			name: < string > ,
			createdDate: < datetime > ,
			active: < boolean >
	}
	...
]														
}	

#### POST /session {-}

*Parameters*
behaviourId: The integer ID of the behaviour to add a session to
name: String name for the session

*Response Format*
id: The integer ID of the session

#### POST /session/<id>/start
*Parameters*
id: The integer ID of the session

*Response Format*
200 OK

#### POST /session/<id> stop
*Parameters*
id: The integer ID of the session

*Response Format*
200 OK

#### POST /session/<id>
*Parameters*
id: The integer ID of the session
name: A string name for the session

*Response Format*
200 OK

#### DELETE /session/<id>
*Parameters*
id: The integer ID of the session

*Response Format*
200 OK


### IPC Messages

Following messages are added to the IPC protocol:

Message JSON fields are forwarded as received from the REST call. Add the following fields:

"create" for REST PUT/POST of new entity
"delete" for REST DELETE
"set" for REST POST of existing entity