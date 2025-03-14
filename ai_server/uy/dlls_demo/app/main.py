# fastapi
# 폴더를 나누는 이유=> 코드의 구조화와 유지보수성 향상을 위해 자주 사용하는 방식

from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

from config.cors_config import CorsConfig
#from convolution_neural_network.controller.cnn_controller import convolutionNeuralNetworkRouter
from ensemble_method.controller.ensemble_method_controller import ensembleMethodRouter
from feature_engineering.controller.feature_engineering_controller import featureEngineeringRouter
#from game_data_fine_tuning.controller.gdft_controller import gameDataFineTuningRouter
#from game_software_analysis.controller.game_software_analysis_controller import gameSoftwareAnalysisRouter
#from gradient_descent.controller.gradient_descent_controller import gradientDescentRouter
#from hyper_parameter.controller.hyper_parameter_controller import hyperParameterRouter
from kmeans.controller.kmeans_controller import kMeansRouter
from mnist.controller.mnist_controller import mnistRouter
from model_regulation.controller.model_regulation_controller import modelRegulationRouter
from openai_basic.controller.openai_basic_controller import openAiBasicRouter
#from principal_component_analysis.controller.pca_controller import principalComponentAnalysisRouter

load_dotenv()
# .env 파일에 정의된 환경변수(HOST, FASTAPI_PORT 등)를 불러옴

app = FastAPI()

CorsConfig.middlewareConfig(app)

# 라우터 추가
app.include_router(featureEngineeringRouter)
app.include_router(ensembleMethodRouter)
app.include_router(kMeansRouter)
app.include_router(mnistRouter)
app.include_router(modelRegulationRouter)
#app.include_router(gradientDescentRouter)
#app.include_router(hyperParameterRouter)
#app.include_router(principalComponentAnalysisRouter)
#app.include_router(convolutionNeuralNetworkRouter)
#app.include_router(gameSoftwareAnalysisRouter)
app.include_router(openAiBasicRouter)
#app.include_router(gameDataFineTuningRouter)
# featureEngineeringRouter는 feature_engineering 모듈의 컨트롤러 파일에 정의된 라우터임
# 이 라우터에 등록된 API 등록 포인트들이 FastAPI에 추가됩니다.


#@app.get("/")
# 루트 경로 ("/")에 대한 간단한 API 엔드포인트입니다.
# 클라이언트가 / 경로에 요청을 보내면, 아래와 같이 {"message": "Data Analysis Test"} 응답을 반환합니다.
#def first_test():
#    return {"message": "Data Analysis Test"}


#if __name__ == "__main__":
#    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
# uvicorn.run :  FastAPI 서버를 실행
# host, port는 .env파일에서 불러온 환경변수를 사용함.


# HOST는 모두에 열려 있고
# FASTAPI_PORT를 통해서 이 서비스가 구동되는 포트 번호를 지정
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))