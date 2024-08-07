_base_ = [
    '../mmdetection/configs/_base_/models/faster-rcnn_r50_fpn.py',
    './kvasir_capsule__coco_detection',
    '../mmdetection/configs/_base_/schedules/schedule_1x.py',
    '../mmdetection/configs/_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=10  # number of classes
        )
    )
)

# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# learning policy
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.0001,
        by_epoch=False,
        begin=0,
        end=4000),
    dict(type='MultiStepLR', by_epoch=True, milestones=[16, 22], gamma=0.1)
]

runner = dict(type='EpochBasedRunner', max_epochs=24)
