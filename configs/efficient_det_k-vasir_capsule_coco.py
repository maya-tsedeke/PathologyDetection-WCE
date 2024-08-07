_base_ = [
    '../mmdetection/projects/EfficientDet/configs/efficientdet_effb3_bifpn_8xb16-crop896-300e_coco.py',
    './kvasir_capsule__coco_detection',
    #'../mmdetection/configs/_base_/schedules/schedule_1x.py',
    #'../mmdetection/configs/_base_/default_runtime.py'
]

model = dict(
    bbox_head=dict(
        num_classes=10  # number of classes
    )
)

# optimizer
optimizer = dict(type='Adam', lr=0.001, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# learning policy
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.0001,
        by_epoch=False,
        begin=0,
        end=4000),
    dict(type='StepLR', by_epoch=True, step=[12], gamma=0.1)
]

runner = dict(type='EpochBasedRunner', max_epochs=36)
