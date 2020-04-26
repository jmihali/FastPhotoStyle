from __future__ import print_function
import torch
import process_cyclic_stylization
from cyclic_photo_wct import CyclicPhotoWCT
from photo_smooth import Propagator

# Load model
p_wct = CyclicPhotoWCT()
p_wct.fw.load_state_dict(torch.load('./PhotoWCTModels/photo_wct.pth'))
p_wct.bw.load_state_dict(torch.load('./PhotoWCTModels/photo_wct.pth'))
p_pro = Propagator()
cuda=0

content_image_path = './images/opernhaus.jpg'
style_image_path = './images/schonbrunn.jpg'
stylized_image_path = './results/example3_stylized.png'
reversed_image_path = './results/example3_reversed.png'


if cuda==1:
    p_wct.cuda(0)

process_cyclic_stylization.cyclic_stylization(
    stylization_module=p_wct,
    smoothing_module=p_pro,
    content_image_path=content_image_path,
    style_image_path=style_image_path,
    content_seg_path=[],
    style_seg_path=[],
    stylized_image_path=stylized_image_path,
    reversed_image_path=reversed_image_path,
    cuda=cuda,
    save_intermediate=True,
    no_post=True,
    do_smoothing=False #added by me, to include or exclude smoothing part
)