for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code: %s" %(e))
   
#NOTE THAT: Using the statement 'except Exception:' instead of 'except Exception as e(or any variable)' will give an error
