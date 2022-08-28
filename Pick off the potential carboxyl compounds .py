#输出结果为excel
#需将待处理的excel放入同一文件夹下，输出结果需放入另一个文件夹
#输出结果格式为特征碎片1，相对百分强度；特征碎片2，相对百分强度；特征中性丢失，产生该特征中性丢失的两个离子的相对百分强度的平均值
import pandas as pd
import os
#input_dir 需要处理的excel的文件夹，不需要具体到文件名，文件夹即可，自动识别该文件夹下所有excel文件
input_dir='C:/Users/lenovo/Desktop/test'
#output_dir 导出excel的文件夹，不需要具体到文件名，文件夹即可，需与input_dir 需要处理的excel的文件夹名称不同
output_dir='C:/Users/lenovo/Desktop/test'
#需要比较的特征碎片和中性丢失
character_fragments1=180.1020
character_fragments2=134.0965
character_loss1=179.0946
files = [f for f in os.listdir(input_dir) if f.endswith('.xlsx')]
for l in range(len(files)):
    print('New file loaded')
    os.chdir(input_dir)
    mass_file = files[l]
    print(files[l])
    mass_df=pd.read_excel(mass_file)
    mass_df['character_fragments1-180.1020']=''
    mass_df['fragments1-180.1020-intensity']=''
    mass_df['character_fragments2-134.0965'] = ''
    mass_df['fragments2-134.0965-intensity'] = ''
    mass_df['character_loss1-179.0946'] = ''
    mass_df['loss1-179.0946-intensity'] = ''
    # print(mass_df)
    shapeMax = mass_df.shape[0]
    for i in range(shapeMax):
        print(i)
        fragments = []
        intensity = []
        fragments_split=mass_df.iloc[i,6].split(' ')
        fragments_num=len(fragments_split)
        for g in range(fragments_num):
            fragments_every=float(fragments_split[g].split(':')[0])
            fragments.append(fragments_every)
            intensity_every = int(fragments_split[g].split(':')[1])
            intensity.append(intensity_every)
        for g in range(fragments_num):
            #对比中性丢失与特征碎片，误差小于5ppm
            if (10**6)*abs(float(fragments[g])-character_fragments1)/character_fragments1< 10:
                mass_df.loc[i, 'character_fragments1-180.1020'] = 'yes'
                mass_df.loc[i,'fragments1-180.1020-intensity']=100*float(intensity[g])/float(max(intensity))
            if (10**6)*abs(float(fragments[g])-character_fragments2)/character_fragments1< 10:
                mass_df.loc[i, 'character_fragments2-134.0965'] = 'yes'
                mass_df.loc[i,'fragments2-134.0965-intensity']=100*float(intensity[g])/float(max(intensity))
            if (10**6)*abs(float(fragments[fragments_num-1])-float(fragments[g])-character_loss1)/character_loss1<10:
                    # print((fragments[m]))
                    # print(fragments[g])
                    mass_df.loc[i, 'character_loss1-179.0946'] = 'yes'
                    mass_df.loc[i, 'loss1-179.0946-intensity'] = 100*(float(intensity[g])/float(max(intensity)))
    output = mass_df
    output_filename = 'output_' + mass_file[0:-5] + '.xlsx'
    os.chdir(output_dir)
    output.to_excel(output_filename, index=False)
