'''一只青蛙一次可以跳上1级台阶,也可以跳上2级台阶.求该青蛙跳上一个n级的台阶总共有多少种跳法   答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008请返回1'''def step(n):    a = 1    b = 2    count = 2    if n == 0:        return 1    elif n <3:        return n    else:        while count < n:            a , b = b, a+b            count +=1        return b%1000000007x = int(input("请输入台阶的数目："))time = step(x)print("青蛙跳N级台阶的跳法有{}种!".format(time))