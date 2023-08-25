import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component'; // Import LoginComponent
import { CustomerDashboardComponent } from './customer/customerdashboard/customerdashboard.component';
import { BookstoreownerdashboardComponent } from './bookstoreowner/bookstoreownerdashboard/bookstoreownerdashboard.component';
import { AdmindashboardComponent } from './admin/admindashboard/admindashboard.component';
import { RegisterUserComponent } from './registeruser/registeruser.component';
import { CartComponent } from './customer/cart/cart.component';
import { OrderhistoryComponent } from './customer/orderhistory/orderhistory.component';
import { BookDetailsComponent } from './customer/bookdetails/bookdetails.component';
import { BookstorebookdetailsComponent } from './bookstoreowner/bookstorebookdetails/bookstorebookdetails.component';
import { AddbookComponent } from './bookstoreowner/addbook/addbook.component';
import { EditbookComponent } from './bookstoreowner/editbook/editbook.component';



const routes: Routes = [
  { path: '', component: LoginComponent },  // Default route is the login page
  { path: 'customer', component: CustomerDashboardComponent }, // Customer dashboard
  { path: 'bookstore', component: BookstoreownerdashboardComponent }, // Bookstore Owner dashboard
  { path: 'admin', component: AdmindashboardComponent }, // Admin dashboard
  { path: 'register', component: RegisterUserComponent },
  { path: 'customer/cart/:id', component: CartComponent },     
  { path: 'customer/order-history/:id', component: OrderhistoryComponent },
  { path: 'customer/book-details/:id', component: BookDetailsComponent },
  { path: 'bookstoreowner/book-details/:id', component: BookstorebookdetailsComponent },
  { path: 'bookstoreowner/addbook', component: AddbookComponent },
  { path: 'bookstoreowner/editbook/:id', component: EditbookComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],  // Configuring the routing module
  exports: [RouterModule]
})
export class AppRoutingModule { }
