def function():
        print("고자 판별기 2.0")
        print("Y: Yes, N: No, Q: Quit")
        while True:
                i=input("당신은 고자입니까? (Y/N/Q) : ")
                if i=="Y":
                        print("그렇군요. 당신은 고자입니다.")
                elif i=="N":
                        print("어쩌라고요. 당신은 고자입니다.")
                elif i!="Q":
                        print("흠... 무슨 말인지는 모르겠지만 당신은 고자입니다.")
                else:
                        print("이렇게 한다고 진짜 꺼질 거라고 생각했나요? 당신은 고자입니다.")
                        print("그럼 어떻게 끄냐고요? 그러게요. 어쨌든 당신은 고자입니다.")           
function()
