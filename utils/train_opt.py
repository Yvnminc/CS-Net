import argparse
import os.path as osp
import os

class TrainOptions:
  def initialize(self):
    parser = argparse.ArgumentParser(description="training script")
    parser.add_argument("--data_path", type= str, default='dataset/DRIVE')
    parser.add_argument("--epochs", type= int, default= 50)
    parser.add_argument("--lr", type= int, default= 0.0001)
    parser.add_argument("--snapshot", type= int, default= 100)
    parser.add_argument("--test_step", type= int, default= 1)
    parser.add_argument("--ckpt_path", type= str, default= "checkpoint/")
    parser.add_argument("--root", type= str, default= "")
    parser.add_argument("--batch_size", type= int, default= 8)

    #parser
    args = parser.parse_args()
    return args
    
  def print_options(self, args):
    message = ''
    message += '----------------- Options ---------------\n'
    for k, v in sorted(vars(args).items()):
        comment = ''
        message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
    message += '----------------- End -------------------'
    print(message)
  
    # save to the disk
    if not osp.exists(args.ckpt_path):
        os.makedirs(args.ckpt_path)
    file_name = osp.join(args.ckpt_path, 'opt.txt')
    with open(file_name, 'wt') as args_file:
        args_file.write(message)
        args_file.write('\n')   


# import argparse
# import os.path as osp
# import os

# class TrainOptions:
#   def initialize(self):
#     parser = argparse.ArgumentParser(description="training script")
#     parser.add_argument("--GPU", type=str, default='0', help="which GPU to use")
#     parser.add_argument("--data", type = str, default= "null")
#     parser.add_argument("--data_path", type = str, default= "null")
#     parser.add_argument('--seed', type=int, default=8, help="random seed")
#     #parser.add_argument('--output_dir', type=str, default='./checkpoints/source')
#     parser.add_argument('--epochs', type=int, default=5, help="max iterations")
#     #parser.add_argument('--hidden_dim', type=int, default=128, help="hidden dimension")
#     # parser.add_argument('--type', type=str, default='val', choices=['full', 'val'])
#     parser.add_argument('--model', type=str, default="null", help="name of model")
#     parser.add_argument('--split_ratio', type = float, default = 0.2, help = 'the split ratio for train and validation set')
#     #parser.add_argument("--snapshot-dir", type=str, default='./checkpoints/model', help="Where to save snapshots of the model.")
#     parser.add_argument('--batch_size', type=int, default=32, help="batch_size")
#     parser.add_argument('--worker', type=int, default=4, help="number of workers")
#     parser.add_argument('--lr', type=float, default=1e-2, help="learning rate")
#     parser.add_argument("--l2_decay", type=float, default=5e-4, help="L2 decay")
#     parser.add_argument("--weight_decay", type = float, default = 1e-5)
#     parser.add_argument("--momentum", type = float, default=0.9)
#     parser.add_argument('--epsilon', type=float, default=1e-5)
#     #parser
#     args = parser.parse_args()
#     return args
    
#   def print_options(self, args):
#     message = ''
#     message += '----------------- Options ---------------\n'
#     for k, v in sorted(vars(args).items()):
#         comment = ''
#         message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
#     message += '----------------- End -------------------'
#     print(message)
  
#     # save to the disk
#     if not osp.exists(args.output_dir):
#         os.makedirs(args.output_dir)
#     file_name = osp.join(args.output_dir, 'opt.txt')
#     with open(file_name, 'wt') as args_file:
#         args_file.write(message)
#         args_file.write('\n')   