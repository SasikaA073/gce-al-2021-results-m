# TODO: IMPORT LIBRARIES
import requests,json,pprint,csv

lap = 200
c = 12100000
b = 9050000

def get_initial_index():
    file = open('index_rounds.txt','r')
    lines = file.readlines()
    initial_index = int(lines[-1].split()[0])
    print(initial_index)
    file.close()
    
    return initial_index


def returnResultJson(_indexNo:int):
    url = "https://result.doenets.lk/result/service/AlResult?index="+ str(_indexNo) +"&nic"
    r = requests.get(url)
    html = r.content
    decodedHTML = html.decode('utf-8')

    #convert string to  object
    json_object = json.loads(decodedHTML)
    # print(r.status_code)
    
    return json_object,r.status_code
m = get_initial_index()
while c > m :
    initial_index = get_initial_index()
    
    with open(f'results_{initial_index}.csv','w',newline="") as csvfile:
        
        csvwriter = csv.writer(csvfile)
        lastIndexNo = initial_index + lap
        for i in range(initial_index,lastIndexNo):
            # print(i)
            try:
                _jsonObject = returnResultJson(i)
                _json_object = _jsonObject[0]
                response_status_code = _jsonObject[1]
                # GET JSON OBJECT VALUES
                districtRank = _json_object['districtRank']
                examination = _json_object['examination']
                indexNo = _json_object['indexNo']
                islandRank = _json_object['islandRank']
                marks = _json_object['marks']
                name = _json_object['name']
                nic = _json_object['nic']
                status = _json_object['status']
                stream = _json_object['stream']
                year = _json_object['year']
                Z_score = _json_object['zScore']

                studentInfo = _json_object['studentInfo']
                subjectResults = _json_object['subjectResults']

                # Subject Results
                subject1Name = subjectResults[0]['subjectName']
                subject1Result = subjectResults[0]['subjectResult']

                subject2Name = subjectResults[1]['subjectName']
                subject2Result = subjectResults[1]['subjectResult']

                subject3Name = subjectResults[2]['subjectName']
                subject3Result = subjectResults[2]['subjectResult']
                print(indexNo)

                commonGeneralTest = subjectResults[3]['subjectName']
                commonGeneralTestResult = subjectResults[3]['subjectResult']

                generalEnglish = subjectResults[4]['subjectName']
                generalEnglishResult = subjectResults[4]['subjectResult']

                # indexNo = i
                csvwriter.writerow([str(i),response_status_code,nic,name,stream,Z_score,districtRank,islandRank,year,subject1Name,subject1Result,subject2Name,subject2Result,subject3Name,subject3Result,commonGeneralTestResult,generalEnglishResult,examination,marks])
            
            except:
                # 
                pass
        with open('index_rounds.txt','a') as version_control_file:
            version_control_file.writelines(f"\n{str(lastIndexNo)}")
        print(f"{initial_index}.csv done")
    m += 1
