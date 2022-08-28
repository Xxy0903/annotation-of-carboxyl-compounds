import pandas as pd

#！！！input_dir1要合并到的excel，input_dir2要与input_dir1合并的文件，output_dir输出文件
input_dir1=r'H:\酒\1. 新做\胺\丹黄酰氯衍生化\原始数据\商品化酒\峰表.xlsx'
input_dir2=r'C:\Users\lenovo\Desktop\新建 Microsoft Excel 工作表.xlsx'
output_dir=r'H:\酒\1. 新做\胺\丹黄酰氯衍生化\原始数据\商品化酒\氨基和酚羟基化合物-result.xlsx'
#！！！mass_error 10ppm rt_error 0.2min，可自己改
mass_error=10
rt_error=0.15
def compared(input_dir1,input_dir2,output_dir):
    df1=pd.read_excel(input_dir1)
    df2=pd.read_excel(input_dir2)
    for n in range(len(list(df2))):
        df1[list(df2)[n]+'-'+str(n)]=None
    num1=df1.shape[0]
    num2=df2.shape[0]
    #！！！第一个文件的mass在哪一列，如在第二列，就是df1.iloc[:,1]，如在第一列就是df1.iloc[:,0]，如在第三列，就是df1.iloc[:,2]
    mass1=df1.iloc[:,1]
    # ！！！第一个文件的rt在哪一列，如在第二列，就是df1.iloc[:,1]，如在第一列就是df1.iloc[:,0]，如在第三列，就是df1.iloc[:,2]
    rt1=df1.iloc[:,0]
    #！！！第二个文件与上述所述
    mass2 = df2.iloc[:,1]
    rt2=df2.iloc[:,0]
    for i in range(num1):
        print(i)
        for l in range(num2):
            if 10**6*abs(mass1[i]-mass2[l])/mass2[l]<mass_error and abs(rt1[i]-rt2[l])<rt_error:
                df1.loc[i,'找到'] = 1
    df1.to_excel(output_dir,index=False)
compared(input_dir1,input_dir2,output_dir)