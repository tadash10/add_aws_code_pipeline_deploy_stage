def add_stage_to_pipeline(pipeline_definition, stage):
    pipeline_definition['stages'].append(stage)
    return pipeline_definition
