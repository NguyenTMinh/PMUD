import os
import tensorflow as tf
from object_detection.builders import model_builder
from object_detection.utils import label_map_util
from object_detection.utils import config_util

#======================= DECLARE VAR =====================
pathToModel = "export/checkpoint"
piplineConfigFile = "export/pipeline.config"
label_map_file = "label_map.pbtxt"
convertedModel = "export/detect.tflite"

#======================== MAIN ============================
configs = config_util.get_configs_from_pipeline_file(piplineConfigFile)
detection_model = model_builder.build(model_config= configs['model'], is_training= False)

ckpt = tf.compat.v2.train.Checkpoint(model= detection_model)
ckpt.restore(os.path.join(pathToModel, 'ckpt-6')).expect_partial()

# convert model
detection_model.save("export/save")