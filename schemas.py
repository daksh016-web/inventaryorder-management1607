from datetime import datetime
from typing import List, Optional
from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field, ConfigDict
# --- PRODUCT SCHEMAS ---
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    sku: str = Field(..., min_length=1, max_length=50)
    price: Decimal = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    description: Optional[str] = Field(None, max_length=500)
class ProductCreate(ProductBase):
    pass
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    sku: Optional[str] = Field(None, min_length=1, max_length=50)
    price: Optional[Decimal] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    description: Optional[str] = Field(None, max_length=500)
class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
# --- CUSTOMER SCHEMAS ---
class CustomerBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=300)
class CustomerCreate(CustomerBase):
    pass
class CustomerUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=300)
class CustomerResponse(CustomerBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
# --- ORDER ITEM SCHEMAS ---
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)
class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price_at_purchase: Decimal
    product: ProductResponse
    model_config = ConfigDict(from_attributes=True)
# --- ORDER SCHEMAS ---
class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate] = Field(..., min_length=1)
class OrderResponse(BaseModel):
    id: int
    customer_id: int
    status: str
    total_amount: Decimal
    created_at: datetime
    customer: CustomerResponse
    items: List[OrderItemResponse]
    model_config = ConfigDict(from_attributes=True)
# --- DASHBOARD METRICS SCHEMA ---
class LowStockProduct(BaseModel):
    id: int
    name: str
    sku: str
    stock: int
class DashboardMetrics(BaseModel):
    total_sales: Decimal
    total_orders: int
    low_stock_count: int
    low_stock_items: List[LowStockProduct]
    total_products: int
    total_customers: int
    model_config = ConfigDict(from_attributes=True)
