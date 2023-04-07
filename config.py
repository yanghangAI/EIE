# Super parameters
clamp = 2.0
channels_in = 3
log10_lr = -4.5
lr = 10 ** log10_lr
weight_decay = 1e-5
init_scale = 0.01

# Model:
device_ids = [0]

# Train:
batch_size = 8
cropsize = 224
betas = (0.5, 0.999)
weight_step = 200
gamma = 0.5

# Val:
cropsize_val = 224
batchsize_val = 2
shuffle_val = False
val_freq = 10


# Dataset
TRAIN_PATH = '/home/yanghang/Dataset/DIV2K/DIV2K_train_HR'
VAL_PATH = '/home/yanghang/Dataset/DIV2K/DIV2K_valid_HR'
format_train = 'png'
format_val = 'png'

# Display and logging:
loss_display_cutoff = 2.0
loss_names = ['train loss', 'val loss', 'lr', 'attack method']
silent = False
live_visualization = False
progress_bar = True


# Saving checkpoints:

MODEL_PATH = 'model/'
checkpoint_on_error = True
SAVE_freq = 50

IMAGE_PATH = 'image/'
IMAGE_PATH_cover = IMAGE_PATH + 'cover/'
IMAGE_PATH_secret = IMAGE_PATH + 'secret/'
IMAGE_PATH_steg = IMAGE_PATH + 'steg/'
IMAGE_PATH_secret_rev = IMAGE_PATH + 'secret-rev/'

