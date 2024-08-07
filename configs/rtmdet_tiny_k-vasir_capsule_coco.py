_base_ = [
    '../mmdetection/configs/rtmdet/rtmdet_tiny_8xb32-300e_coco.py../_base_/models/rtmdet_tiny_8xb32-300e_coco.py',
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
optimizer = dict(type='SGD', lr=0.001, weight_decay=0.0005)
optimizer_config = dict(grad_clip=None)

# learning policy
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.0001,
        by_epoch=False,
        begin=0,
        end=4000),
    dict(type='CosineAnnealing', by_epoch=True, T_max=330, eta_min=0)
]

runner = dict(type='EpochBasedRunner', max_epochs=330)
