var express = require('express');
var app     = express();
var fs = require('fs');

var stops = require('./public/busStops.json');

var port    = process.env.PORT || 4000;

app.use("/assets",  express.static(__dirname + '/public'));

app.use('/',function(req,res,next){ //for reSort JSON query and display
	console.log('Request Url:'+req.url);
	next();
});

app.get('/',function(req,res){
	res.send(JSON.stringify(stops,null,3));
});

app.get('/keys', function(req,res){
	var keys = [];
	for(var k in stops[0]){
		keys.push(k);
	}
	res.send(keys);
});

app.get('/:index/:value?', function(req,res){
	res.setHeader('Content-Type', 'application/json');
	var check = req.params.value;
	if(!check){
		res.send(JSON.stringify(stops,null,3));
	}
	else{
		check = check.toUpperCase();
		var index = req.params.index;
		var matches={};
		matches[check]=[];
		for (i = 0; stops.length > i; i += 1) {
			if(typeof stops[i][index] !=="undefined"){
				if (stops[i][index].toUpperCase().indexOf(check) >= 0) {
        	 		matches[check].push(stops[i]);
        	 	};
			}
			else{
				console.log('undefined entry');	
			};
		};
		res.send(JSON.stringify(matches[check],null,3));
	};
});

app.listen(port);
