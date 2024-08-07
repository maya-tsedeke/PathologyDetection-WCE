_base_ = [
    '../mmdetection/configs/soft_teacher/soft-teacher_faster-rcnn_r50-caffe_fpn_180k_semi-0.1-coco.py',
    '../mmdetection/configs/_base_/datasets/coco_detection.py',
    './kvasir_capsule__coco_detection',
    #'../mmdetection/configs/_base_/schedules/schedule_1x.py',
    #'../mmdetection/configs/_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=10  # number of classes
        )
    )
)
# training schedule for 180k
train_cfg = dict(
    type='IterBasedTrainLoop', max_iters=90000, val_interval=3000)
val_cfg = dict(type='TeacherStudentValLoop')
test_cfg = dict(type='TestLoop')

# learning rate policy
param_scheduler = [
    dict(
        type='LinearLR', start_factor=0.001, by_epoch=False, begin=0, end=500),
    dict(
        type='MultiStepLR',
        begin=0,
        end=90000,
        by_epoch=False,
        milestones=[30000, 70000],
        gamma=0.1)
]

# optimizer
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=dict(type='SGD', lr=0.001, momentum=0.6, weight_decay=0.0005))
