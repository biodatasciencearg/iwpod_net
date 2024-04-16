import numpy as np
from iwpodnet.src.keras_utils import load_model
from iwpodnet.src.keras_utils    import  detect_lp_width
from iwpodnet.src.utils          import  im2single

# Image type (car, truck, bus, bike or fullimage)
class IwpodNet:
    
    def __init__(self, lp_threshold = 0.35 , ocr_input_size = [80, 240]):
        #
        #  Parameters of the method
        self.lp_threshold= lp_threshold
        self.ocr_input_size= ocr_input_size
        # 
        #
        #  Loads network and weights
        #
        self.iwpod_net = load_model('iwpod_net')
        

    
    def get_roi(self, Ivehicle, vtype="fullimage", verbose=0):
        """
        Method to obtain Region of interes a.k.a licence_plate.
        Ivehicle :array  numpy array with frame.
        vtype:str  vehicle categories in 'car', 'bus', 'truck'"""
        
        # Define results list.
        results=[]
        
        iwh = np.array(Ivehicle.shape[1::-1],dtype=float).reshape((2,1))

        if (vtype in ['car', 'bus', 'truck']):
            #
            #  Defines crops for car, bus, truck based on input aspect ratio (see paper)
            #
            ASPECTRATIO = max(1, min(2.75, 1.0*Ivehicle.shape[1]/Ivehicle.shape[0]))  # width over height
            WPODResolution = 256# faster execution
            lp_output_resolution = tuple(self.ocr_input_size[::-1])

        elif  vtype == 'fullimage':
            #
            #  Defines crop if vehicles were not cropped 
            #
            ASPECTRATIO = 1 
            WPODResolution = 480 # larger if full image is used directly
            lp_output_resolution =  tuple(self.ocr_input_size[::-1])
        else:
            #
            #  Defines crop for motorbike  
            #
            ASPECTRATIO = 1.0 # width over height
            WPODResolution = 208
            lp_output_resolution = (int(1.5*self.ocr_input_size[0]), self.ocr_input_size[0]) # for bikes, the LP aspect ratio is lower

        #
        #  Runs IWPOD-NET. Returns list of LP data and cropped LP images
        #

        Llp, LlpImgs,_ = detect_lp_width(self.iwpod_net
                                         , im2single(Ivehicle)
                                         , WPODResolution*ASPECTRATIO, 2**4
                                         , lp_output_resolution
                                         , self.lp_threshold
                                         , verbose=verbose)
        for i, img in enumerate(LlpImgs):
            #
            #  Draws LP quadrilateral in input image
            #
            pts = Llp[i].pts * iwh
            #draw_losangle(Ivehicle, pts, color = (0,0,255.), thickness = 2)

            #  Adding results to output
            #
            results.append((255*img).astype(np.uint8))
        return results