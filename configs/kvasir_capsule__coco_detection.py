# This configuration file is derived from the MMdetection repository
# Link to original repository: https://github.com/open-mmlab/mmdetection

#_base_ = '../_base_/datasets/coco_detection.py'

classes = (
    'Ampulla of Vater', 'Angiectasia', 'Blood - fresh', 'Blood - hematin',
    'Erosion', 'Erythema', 'Foreign Body', 'Lymphangiectasia', 'Polyp', 'Ulcer'
)
data_root = 'data/k-vasir_capsule/'

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(640, 640), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='MultiScaleFlipAug', img_scale=(640, 640), flip=False,
         transforms=[
             dict(type='Resize', keep_ratio=True),
             dict(type='RandomFlip'),
             dict(type='Normalize', **img_norm_cfg),
             dict(type='Pad', size_divisor=32),
             dict(type='ImageToTensor', keys=['img']),
             dict(type='Collect', keys=['img']),
         ])
]

train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    dataset=dict(
        #type=dataset_type,
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file='annotations/instances_train.json',
        img_prefix='train2017/'
    )
)

val_dataloader = dict(
    batch_size=1,
    num_workers=2,
    dataset=dict(
        #type=dataset_type,
        test_mode=True,
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file='annotations/instances_val.json',
        img_prefix='val/'
    )
)

test_dataloader = dict(
    batch_size=1,
    num_workers=2,
    dataset=dict(
        #type=dataset_type,
        test_mode=True,
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file='annotations/instances_val.json',
        img_prefix='val/'
    )
)
