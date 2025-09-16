import pandas as pd

data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '数学': [85, 92, 78, 88, 95],
    '英语': [90, 88, 85, 92, 80],
    '物理': [75, 80, 88, 85, 90]
}

score=pd.DataFrame(data,index=[1,2,3,4,5])
print(score)
score['总分']=score[['数学','英语','物理']].sum(axis=1)
print(score)
score['avarge']=score['总分']/3
print(score)
score['ave2']=score[['数学','英语','物理']].mean(axis=1)
print(score)
print(score[(score['数学']>90)|(score['英语']>85)])
print(score.sort_values('总分',ascending=False).head(3))
print(score.nlargest(3,columns=['总分']))