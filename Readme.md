# Debiasing Skin Cancer Detection

## Annotation

### Data

You can download the link for zipped combine dataset using [Drive Link](https://drive.google.com/file/d/11hP_2PjwkzgUbaOyXHn7EEWDURJZPqpv/view?usp=sharing)

The data folder should be containing the HAM10000_metadata.csv and the two folders containing the images that is unzipped from the link [Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T). Make sure to download both the **HAM10000_images_part_1/** and **HAM10000_images_part_2/** folder.  

Combine the imgs into one folder and called imgs under data.  



To start the flask app 
```
python3 app.py
```
This will open up on the browser http://127.0.0.1:5000/


## References 
* [Github Repo](https://github.com/alceubissoto/debiasing-skin)
* [Paper](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w42/Bissoto_Debiasing_Skin_Lesion_Datasets_and_Models_Not_So_Fast_CVPRW_2020_paper.pdf)