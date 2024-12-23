export interface ProductState {
    productList: Product[]
    product: Product | null
  }
  
  export interface Product {
    productId: number
    productName: string
    productPrice: string
    productDescription: string
    productImage: string
    registeredDate: string
    updatedDate: string
  }
  