import json
import settings as env
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication via IAM
authenticator = IAMAuthenticator(env.NATURAL_LANGUAGE_UNDERSTANDING_IAM_APIKEY)
service = NaturalLanguageUnderstandingV1(version='2018-03-16', authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

def analise(tweet):
    '''
	PT-BR: 
	Envia o texto para ser analisado pelo Watson NLU e rertona o Json com a analise de acordo com as Features inseridas
	EN: 
	Send the text to be analyzed by Watson NLU and return Json with the analysis according to the inserted Features
	'''
    response = service.analyze(
        text= tweet,
        features=Features(entities=EntitiesOptions(),
         keywords=KeywordsOptions(), emotion=EmotionOptions(), sentiment=SentimentOptions())).get_result()
    
    return(json.dumps(response, indent=2))

    