import requests as req,os
from dotenv import load_dotenv,find_dotenv
from requests import session
import logging as log


payload={'action':'login',
        'username':os.environ.get("KAGGLE_USERNAME"),
         'password':os.environ.get("KAGGLE_PASSWORD")
        }
def extract_data(url,file_path):
    with session() as s:
        s.post('https://www.kaggle.com/account/login',data=payload)
        with open(file_path,'wb') as file: 
            response=s.get(url,stream=True)
            for block in response.iter_content(1024):
                file.write(block)
#project_dir corresponds to the main project directory
def main(project_dir):
    #get logger
    logger=log.getLogger(__name__)
    logger.info('getting raw data')
    
    test_url="https://www.kaggle.com/c/3136/download/test.csv"
    train_url="https://www.kaggle.com/c/3136/download/train.csv"

    raw_data_path=os.path.join(project_dir,'data','raw')
    train_data_path=os.path.join(raw_data_path,'train.csv')
    test_data_path=os.path.join(raw_data_path,'test.csv')
    
    extract_data(train_url,train_data_path)
    extract_data(test_url,test_data_path)
    logger.info('data downloaded')
    
if __name__=='__main__':
    project_dir=os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir)
    print(project_dir)
    
    #setup logger
    log_format='%(asctime)s - %(name)s -  %(levelname)s -  %(message)s'
    log.basicConfig(level=log.INFO,format=log_format)
    
    
    load_dotenv(find_dotenv())
    main(project_dir)