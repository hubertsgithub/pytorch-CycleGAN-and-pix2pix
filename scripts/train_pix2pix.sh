python train.py --dataroot ./datasets/shapenet_chairs_single_label --name mattrans_chairs_single_label_solidbws_pix2pix --model pix2pix --which_model_netG unet_256 --which_direction BtoA --lambda_A 100 --dataset_mode aligned --no_lsgan --norm batch --pool_size 0 --niter 200 --niter_decay 200
