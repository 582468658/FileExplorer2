function BE_InitFile_faker()
{
	window.files =
	[
		{
			"id": 0,
			"parentId": "",
			"level": 0,
			"name": "root",
			"type": "folder",
			"size": "",
			"modifyTime": 2018,
			"userId": 1111
		},
		{
			"id": 1,
			"parentId": 0,
			"level": 1,
			"name": "a",
			"type": "folder",
			"size": "",
			"modifyTime": 2018,
			"userId": 1111
		},
		{
			"id": 2,
			"parentId": 1,
			"level": 2,
			"name": "2",
			"type": "file",
			"size": "100KB",
			"modifyTime": 2018,
			"userId": 1111
		},
			{
			"id": 3,
			"parentId": 0,
			"level": 1,
			"name": "b",
			"type": "folder",
			"size": "",
			"modifyTime": 2018,
			"userId": 1111
		},
		{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
				{
			"id": 4,
			"parentId": 0,
			"level": 1,
			"name": "aa",
			"type": "png",
			"size": "200MB",
			"modifyTime": 2018,
			"userId": 1111
		},
			{
			"id": 5,
			"parentId": 0,
			"level": 1,
			"name": "bb",
			"type": "file",
			"size": "1B",
			"modifyTime": 2018,
			"userId": 1111
		}
	];
}

function BE_CreateFolder_fake(parentFile)
{
      var newFile = new Object();
      newFile.id = "";
      newFile.parentId = parentFile.id;
      newFile.level = parentFile.level + 1;
      newFile.name = "untitle";
      newFile.type = "folder";
      newFile.modifyTime = "";
      newFile.userId = getCookie("userId");
      return newFile;
}

function getCookie_faker(name)
{
	if("userId" == name) return "9978";
	return "getCookie_faker return default";
}