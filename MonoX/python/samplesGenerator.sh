#!/bin/bash

#monoZp=(/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_monozp/flat/*)
#monoHs=(/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_monohs/flat/*)

#monoX=("${monoZp[@]}" "${monoHs[@]}")
monoX="/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_v2/flat"

if [ -e samples.py ];then
    rm samples.py
fi

#total=${#monoX[@]}
total=`(eval cd ${monoX}; ls -l | wc -l )`
echo "Total signals found = $total"
#for med in `ls ${monoX[@]}`
for med in `ls ${monoX}`
do
    species=`(echo $med | awk -F "-" '{print $1}')`

    if [ $species == "BBbarDM_MZprime" ];then
        sp="hsDM"
    elif [ $species == "DiJetsDM_MZprime" ];then
        sp="ZpDM"
    else
	continue
    fi


    filename=$(basename "$med")
    filename="${filename%.*}"
    #species=`(echo $filename | awk -F "-" '{print $1}')`
    mmed=`(echo $filename | awk -F "-" '{print $2}' | awk -F "_" '{print $1}')`
    mhs=`(echo $filename | awk -F "-" '{print $3}' | awk -F "_" '{print $1}')`
    mdm=`(echo $filename | awk -F "-" '{print $4}')`
    echo ${species}
    echo "Zp = ${mmed} GeV, hs = ${mhs} GeV, DM = ${mdm} GeV"

    var=$((var+1))

    if [ $var -eq 1 ];then
	echo "sample = {" > samples1.py
	echo "samples = { " > samples2.py
    fi

    echo -e "\t'${filename}': {"    >> samples1.py
    echo -e "\t'nevents' : 250000," >> samples1.py
    echo -e "\t'xsec'    : 1.,"     >> samples1.py
    echo -e "\t'matcheff': 1.,"     >> samples1.py
    echo -e "\t'kfactor' : 1.,"     >> samples1.py
    echo -e "\t\t},"                >> samples1.py

    ##############################################
    
    echo -e "\t'${sp}-${mmed}-${mhs}-${mdm}' : {"            >> samples2.py
    echo -e "\t'order' : 1001,"                           >> samples2.py
    echo -e "\t'files' : ['${filename}'],"                >> samples2.py
    echo -e "\t'fillcolor' : 623,"                        >> samples2.py
    echo -e "\t'fillstyle' : 3005,"                       >> samples2.py
    echo -e "\t'linecolor' : 623,"                        >> samples2.py
    echo -e "\t'linewidth' : 3,"                          >> samples2.py
    echo -e "\t'linestyle' : 1,"                          >> samples2.py
    #echo -e "\t'label' : \"${sp}-${mmed}-${mhs}-${mdm}\"," >> samples2.py
    echo -e "\t'label' : \"M(Z^{\'},hs,#chi)=(${mmed},${mhs},${mdm}) GeV\"," >> samples2.py
    echo -e "\t'weight': 1.,"                             >> samples2.py
    echo -e "\t'plot': True,"                             >> samples2.py
    echo -e "   },"                                       >> samples2.py

#    if [ ${var} -eq ${total} ];then
#        echo -e "}"                 >> samples1.py
#	echo -e "}"                 >> samples2.py
#    fi

done

echo -e "}"                 >> samples1.py 
echo -e "}"                 >> samples2.py      

cat samples1.py samples2.py > samples.py
rm samples1.py samples2.py