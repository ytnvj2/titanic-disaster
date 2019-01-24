import kaggle,os
import logging as log
def extract_data(competition,file,file_path):
    connect=kaggle.KaggleApi()
    connect.authenticate()
    connect.competition_download_file(competition,file_name=file,path=file_path)
#project_dir corresponds to the main project directory
def main(project_dir):
    #get logger
    logger=log.getLogger(__name__)
    logger.info('getting raw data')
    data_path=os.path.join(project_dir,'data','raw')
    competition='titanic'
    extract_data(competition,'train.csv',data_path)
    extract_data(competition,'test.csv',data_path)
    logger.info('data downloaded')
    
if __name__=='__main__':
    project_dir=os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir)
    print(project_dir)
    #setup logger
    log_format='%(asctime)s - %(name)s -  %(levelname)s -  %(message)s'
    log.basicConfig(level=log.INFO,format=log_format)
    main(project_dir)