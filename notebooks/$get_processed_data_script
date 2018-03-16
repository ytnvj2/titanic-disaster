import pandas as pd,numpy as np,os
def read_data():
    #setting path of the files
    raw_data_path=os.path.join(os.path.pardir,'data','raw')
    train_data_path=os.path.join(raw_data_path,'train.csv')
    test_data_path=os.path.join(raw_data_path,'test.csv')
    #read data and set all default values
    train_df=pd.read_csv(train_data_path,index_col='PassengerId')
    test_df=pd.read_csv(test_data_path,index_col='PassengerId')
    test_df['Survived']=-888
    df=pd.concat((test_df,train_df),axis=0)
    return df
def process_data(df):
    #using method chaning
    return (df
            #use assign method to create new feature
            .assign(Title=lambda x: x.Name.map(getTitle))
            #pipe method used to apply function on dataframe
            .pipe(fill_missing_vals)
            #feature addition
            .assign(Fare_bin=lambda x: pd.qcut(x.Fare,4,labels=['very low','medium','high','very high']))
            .assign(AgeState=lambda x: np.where(x.Age<18,'Child','Adult'))
            .assign(FamilySize=lambda x: x.Parch+x.SibSp+1 )
            .assign(IsMother=lambda x:np.where((x.Age>18)&(x.Sex=='female')&(x.Title!='Miss')&(x.Parch>0),1,0) )
            .assign(Cabin=lambda x: np.where(x.Cabin=='T',np.nan,x.Cabin))
            .assign(Deck=lambda x: x['Cabin'].map(get_deck))
            #feature encoding
            .assign(IsMale=lambda x: np.where(x.Sex=='male',1,0))
            .pipe(pd.get_dummies,columns=['Deck','Pclass','Title','Fare_bin','Embarked','AgeState'])
            #drop columns, method chaining doesn't require inplace attribute
            .drop(['Cabin','Name','Ticket','Parch','SibSp','Sex'],axis=1)
            .pipe(reorder_column))
            
def fill_missing_vals(df):
    #Embarked missing values filled
    df.Embarked.fillna('C',inplace=True)
    #Fare missing values filled
    df.loc[df.Fare.isnull(),'Fare']=df[(df.Embarked=='S')&(df.Pclass==3)&(df.Sex=='male')&(df.Age>60)].Fare.median()
    #Age missing values filled
    df.Age.fillna(df.groupby('Title').Age.transform('median'),inplace=True)
    return df
    
def getTitle(name):
    title_dict={'mr':'Mr', 'mrs':'Mrs', 'miss':'Miss', 'master':'Master', 'ms':'Miss', 'col':'Officer', 'rev':'Sir', 'dr':'Officer', 'dona':'Lady',
       'don':'Sir', 'mme':'Lady', 'major':'Officer', 'lady':'Lady', 'sir':'Sir', 'mlle':'Lady', 'capt' :'Officer',
       'the countess':'Lady', 'jonkheer':'Sir'}
    get_name_with_title=name.split(',')[1]
    title=get_name_with_title.split('.')[0]
    return title_dict[title.strip().lower()]
def get_deck(cabin):
    return np.where(pd.notnull(cabin),str(cabin)[0].upper(),'Z')
            
def reorder_column(df):
    columns=[col for col in df.columns if col!='Survived']
    columns +=['Survived']
    df=df[columns]
    return df

def write_data(df):
    # Saving and writing a dataframe to a file
    processed_data_path=os.path.join(os.path.pardir,'data','processed')
    train_data_path=os.path.join(processed_data_path,'train.csv')
    test_data_path=os.path.join(processed_data_path,'test.csv')
    # writing data to csv file
    df.loc[df.Survived!=-888].to_csv(train_data_path)
    columns=[col for col in df.columns if col!='Survived']
    df.loc[df.Survived==-888,columns].to_csv(test_data_path)
    
if __name__=='__main__':
    df=read_data()
    df=process_data(df)
    write_data(df)