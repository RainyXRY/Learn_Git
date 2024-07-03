import warnings
warnings.filterwarnings("ignore")

# 非侵入式设置HuggingFace的下载镜像
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from transformers import pipeline

# 指定模型版本  
model_name = "bert-base-uncased@huggingface/bert-base-uncased-v2"  
nlp = pipeline("sentiment-analysis", model=model_name)

# 今天的修改
a = 1
b = 2

branch = "matlab"