_base_ = [
    '../mmdetection/configs/ssd/ssdlite_mobilenetv2-scratch_8xb24-600e_coco.py',
    './kvasir_capsule__coco_detection',
    #'../mmdetection/configs/_base_/schedules/schedule_1x.py',
    #'../mmdetection/configs/_base_/default_runtime.py'
]

# Modify model settings for the custom number of classes
model = dict(
    bbox_head=dict(
        num_classes=10  # Set the number of classes to 10 if you used k-vasir capsule dataset without modification
    )
)

# training schedule
max_epochs = 140
train_cfg = dict(max_epochs=max_epochs, val_interval=10)

# learning rate scheduler
param_scheduler = [
    dict(
        type='LinearLR', start_factor=0.0001, by_epoch=False, begin=0, end=500),
    dict(
        type='CosineAnnealingLR',
        begin=0,
        T_max=max_epochs,
        end=max_epochs,
        by_epoch=True,
        eta_min=0)
]

# optimizer
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=dict(type='SGD', lr=0.001, momentum=0.6, weight_decay=0.001))