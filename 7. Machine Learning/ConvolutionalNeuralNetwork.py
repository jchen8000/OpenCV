import numpy as np

def convolution1d():
    f = np.array([1, 2, 1])
    g = np.array([3, 0, 2, 4, 2, 1])
    conv = np.convolve(f, g, mode = 'valid')
    print("f =", f)
    print("g =", g)
    print("f*g =", conv)

def convolution2d(image, kernel, stride=[1,1], padding=[0,0]):
    p_h, p_w = padding
    s_h, s_w = stride
    image = np.pad(image,
                   [(p_h, p_h), (p_w, p_w)],
                   mode='constant',
                   constant_values=0)

    k_h, k_w = kernel.shape
    i_h, i_w = image.shape

    output_h = (i_h - k_h) // s_h + 1
    output_w = (i_w - k_w) // s_w + 1

    output = np.zeros((output_h, output_w))

    for y in range(0, output_h):
        for x in range(0, output_w):
            c = image[y*s_h : y*s_h+k_h, x*s_w : x*s_w+k_w]
            c = np.multiply(c, kernel)
            output[y][x] = np.sum(c)
    return output

def maxpooling2d(image, kernel=[3,3],
                 stride=[0,0], padding=[0,0]):
  p_h, p_w = padding
  s_h, s_w = stride
  k_h, k_w = kernel
  image = np.pad(image,
                 [(p_h, p_h), (p_w, p_w)],
                 mode='constant',
                 constant_values=0)
  i_h, i_w = image.shape
  output_h = -(-i_h // (k_h + s_h))
  output_w = -(-i_w // (k_w + s_w))
  output = np.zeros((output_h, output_w))
  for y in range(0, output_h):
    for x in range(0, output_w):
      y_, x_ = y*(s_h+k_h), x*(s_w+k_w)
      c = image[y_: y_+k_h, x_ : x_+k_w]
      output[y][x] = np.amax(c)
  return output


if __name__ == "__main__":
    print("Convolution for 1D array")
    convolution1d()

    print("\nConvolution for 2D array")
    image = np.array([[1, 3, 1, 0, 2, 1, 0],
                      [1, 1, 1, 2, 1, 2, 1],
                      [2, 1, 9, 9, 8, 2, 0],
                      [0, 2, 9, 1, 9, 0, 1],
                      [1, 0, 9, 0, 8, 2, 1],
                      [3, 1, 1, 2, 0, 2, 2],
                      [1, 3, 1, 3, 3, 2, 0]])
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 0, 1]])
    conv2d = convolution2d(image, kernel)
    print(conv2d)

    print("\nMax Pooling")
    conv2d = convolution2d(image, kernel,
                           padding=[1, 1])
    maxp2d = maxpooling2d(conv2d, kernel=[3, 3])
    print(maxp2d)
