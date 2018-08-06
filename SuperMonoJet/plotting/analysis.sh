#Test bench

#rm -rf zee zmm wen wmn tmn ten
#rm -rf zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail

decide=1 # 0-fail; 1-pass
inclusive=1

if [ $decide -eq 1 ];then

    if [ $inclusive -eq 1 ]; then
	#echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 25 --region
	#mkdir nofjmasscut_MIN25
	#mv zee zmm wen wmn tmn ten nofjmasscut_MIN25
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --fromlimit --region
	mkdir nofjmasscut-fromlimit
	mv zee zmm wen wmn tmn ten nofjmasscut-fromlimit
    else
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 25 --region
	mkdir nofjmasscut_MIN25
	mv zee zmm wen wmn tmn ten nofjmasscut_MIN25
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 25 --masscut2 75 --region
	mkdir mass0_1
	mv zee zmm wen wmn tmn ten mass0_1
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 50 --masscut2 75 --region
	mkdir mass0_2
	mv zee zmm wen wmn tmn ten mass0_2
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 75 --masscut2 100 --region
	mkdir mass1
	mv zee zmm wen wmn tmn ten mass1
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 100 --masscut2 150 --region
	mkdir mass2
	mv zee zmm wen wmn tmn ten mass2
	echo zee zmm wen wmn tmn ten | xargs -n 1 -P 8 python analysis.py --masscut1 150 --masscut2 3000 --region
	mkdir mass3
	mv zee zmm wen wmn tmn ten mass3
    fi
else

    if [ $inclusive -eq 1 ]; then
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 25 --region
	mkdir nofjmasscut_fail_MIN25
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail nofjmasscut_fail_MIN25
    else
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 25 --region
	mkdir nofjmasscut_fail_MIN25
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail nofjmasscut_fail_MIN25
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 25 --masscut2 75 --region
	mkdir mass0_1_fail
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail mass0_1_fail
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 50 --masscut2 75 --region
	mkdir mass0_2_fail
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail mass0_2_fail
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 75 --masscut2 100 --region
	mkdir mass1_fail
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail mass1_fail
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 100 --masscut2 150 --region
	mkdir mass2_fail
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail mass2_fail
	echo zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail | xargs -n 1 -P 8 python analysis.py --masscut1 150 --masscut2 3000 --region
	mkdir mass3_fail
	mv zee_fail zmm_fail wen_fail wmn_fail tmn_fail ten_fail mass3_fail
    fi
fi