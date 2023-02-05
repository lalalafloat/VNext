import json

def view_tao_json():
    json_path = '/media/ubuntu/56b20cc5-cf3c-4bbf-9364-db7e2f5e2e94/wby_workspace/VNext_LTL/datasets/tao/annotations/new_baseline_all/tao_train_img_30fps_coco_trainall_nopseudo_iou_refine.json'

    with open(json_path, 'r') as f:
        data = json.load(f)
    print(data['annotations'][100])
    print(data['images'][100])
    
    print(data['categories'])
    for img in data['images']:
        if 'video_id' not in img.keys():
            print(img)
            break 

    # coco_path = 'datasets/coco/annotations/instances_train2017_agn.json'
    # with open(coco_path, 'r') as f:
    #     coco = json.load(f)
    # coco_img_name = coco['images'][100]['']
    

def change_json_unique():
    json_path = '/media/ubuntu/56b20cc5-cf3c-4bbf-9364-db7e2f5e2e94/wby_workspace/VNext_LTL/datasets/tao/annotations/new_baseline_all/tao_train_img_30fps_coco_trainall_nopseudo_iou_refine.json'

    with open(json_path, 'r') as f:
        data = json.load(f)

    annos = []
    for idx,anno in enumerate(data['annotations']):
        anno['id'] = idx + 1
        annos.append(anno)
    data['annotations'] = annos
    for img in data['images']:
        if 'video_id' in img.keys():
            img['file_name'] = 'tao/frames/' + img['file_name']
        else:
            img['file_name'] = 'coco/train2017/' + img['file_name']
    new_path = 'datasets/tao/annotations/right_json/coco_train_tao_30fps_pse.json'
    with open(new_path, 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':

    # view_tao_json()
    change_json_unique()
    pass

# {'file_name': 'datasets/tao/frames/train/YFCC100M/v_f69ebe5b731d3e87c1a3992ee39c3b7e/frame0394.jpg', 'image_id': 1000003, 'segmentation': [[418, 164, 458, 164, 458, 225, 418, 225]], 'bbox': [418, 164, 40, 61], 'id': 15000000000000100, 'category_id': 1, 'gen': 1, 'longscore': 0.2817420959472656, 'iou_score': 0, 'iscrowd': 0, 'isgt_wby': 0, 'epoch0_gt': 1}
# {'id': 1000100, 'video': 'train/YFCC100M/v_f69ebe5b731d3e87c1a3992ee39c3b7e', '_scale_task_id': 'non', 'width': 640, 'height': 480, 'file_name': 'train/YFCC100M/v_f69ebe5b731d3e87c1a3992ee39c3b7e/frame0491.jpg', 'frame_index': 100, 'license': 0, 'video_id': 0}
# [{'frequency': 'r', 'id': 1, 'synset': 'acorn.n.01', 'image_count': 0, 'instance_count': 0, 'synonyms': ['acorn'], 'def': 'nut from an oak tree', 'name': 'coco'}]

# {'license': 3, 'file_name': '000000391895.jpg', 'coco_url': 'http://images.cocodataset.org/train2017/000000391895.jpg', 'height': 360, 'width': 640, 'date_captured': '2013-11-14 11:18:45', 'flickr_url': 'http://farm9.staticflickr.com/8186/8119368305_4e622c8349_z.jpg', 'id': 391895}