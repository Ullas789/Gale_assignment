class Category:
    def __init__(self,cat_name,cat_url,cat_img,cat_description,parent_category):
        self.cat_name=cat_name
        self.parent_category=parent_category #sub-category
        self.cat_url=cat_url
        self.cat_img=cat_img
        self.cat_description=cat_description

class Brand:
    def __init__(self,b_name,b_logo,b_website):
        self.b_name=b_name
        self.b_logo=b_logo
        self.b_website=b_website
    
       
class Product:
    def __init__(self,p_name,p_url,p_img,p_description,category,brand):
        self.brand=brand
        self.category=category #category
        self.p_name=p_name
        self.p_url=p_url
        self.p_img=p_img
        self.p_description=p_description
    def information(self):
        print(f"\nProduct_Information\n name: {self.p_name} \n website: {self.p_url}\n image: {self.p_img} \n Description: {self.p_description}\n")
      
    # def display_brand(self):
    #     print(f"Brand_Information \n brand_name: {self.brand}\n")
    def display(self):
        self.information()
        # self.display_brand()
        print(f"Categories")
       
        
        category=self.category
        
        # print(category.parent_category.cat_name)
        print(self.p_name)
        while(category.parent_category!=None):
            print(category.cat_name ,end='->')
            category=category.parent_category
        print(category.cat_name)

def filter_leaf(category,products):
   
    leaf=[]
    for product in products:
        p=product.category
        
        # while(p.cat_name!=category.cat_name ):
        #     print(product.p_name)
        #     p=p.parent_category
        # # print(product.p_name)
        while p:
            if p==category:
                leaf.append(product.p_name)
                break
            p=p.parent_category
    print(leaf)
       
        
 
        
            
   
    

            
    
     
#brand

apple=Brand("Apple","apple.logo","apple.com")
samsung=Brand("Samsung","samsung.logo","samsung.com")

#mobile




Electronics=Category("electronics","electronics.com","electronics.jpeg","electronics",None)
Furniture=Category("furni","furni.com","furni.jpeg","furni.descr",None)

w_m=Category("W-m","w-m.com","w-m.jpeg","w-m.descr",Electronics)
whirpool=Product('whrpl',"whrpl.com","whrpl.jpeg","whrpl",w_m,None)

mobile=Category("mobile","mobile.com","mobile.jpeg","mobile_description",Electronics)
android=Category("android","android.com","android.jpeg","android_description",mobile)
iphone=Category("iphone","iphone.com","iphone.jpeg","iphone",mobile)

m32=Product("m32","m32.com","m32.jpeg","m32_description",android,samsung)
m31=Product("m31","m31.com","m31.jpeg","m31_description",android,samsung)

iphone15=Product('iphone_15',"i_15.com","i_15.jpeg","iphone15_pro_max",iphone,apple)
iphone16=Product('iphone_16',"i_16.com","i_16.jpeg","iphone16_pro",iphone,apple)
# m32.display()
# m31.display()
# iphone15.display()
# iphone16.display(
filter_leaf(mobile,[m31,iphone15,iphone16,m32])
# filter_leaf(iphone,[m31,iphone15,iphone16,m32])
