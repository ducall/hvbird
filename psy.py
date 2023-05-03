//模型运算的卷积结果
for i in range(outpuChannel) :
    while ((row+kernelSize-1) < rowMax): 
    while ((column+kernelSize-1) < columnMax):
      sum = bias
      for i in range(kernelSize):
        for j in range(kernelSize):
          for k in range(inputCh/2):
            sum = sum + featureMap[row+i][column+j][k] * weight[i][j][k]   
            print("input feature0: ",featureMap[row][column][i])
            print("weight0: ", weight[0][0][i])    
      print("sum0: ", sum)
      rslt.append(sum)
      column = column + xStride
    column = 0
//将DUT中打印的中间结果值输入到该程序中
for line in  open("./ParticalSum.txt","r") //ParticalSum.txt为DUT打印的中间结果
//逐个对比   
   for i in range (56*56) :
    if(data1[i] !=data2[i][0]) :
      print("after check is false")
      return 0
//打印中间结果与模型中不同的结果
for i in range (56*56) :
  if(outDiff[i] !=data1[i][0]) :
    print(i,(outDiff[i] - data1[i][0]))
    afcsv