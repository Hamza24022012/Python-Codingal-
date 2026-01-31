student_data={
    "id1":{
        "name":"Ali",
        "class":"V",
        "subjects":["english","math","physics"]
    },
    "id2":{
        "name":"Zara",
        "class":"VI",
        "subjects":["english","math","physics"]
    },
    "id3":{
        "name":"Zara",
        "class":"VI",
        "subjects":["english","math","physics"]
},
    "id4":{
        "name":"David",
        "class":"VI",
        "subjects":["english","math","physics"]
}
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)