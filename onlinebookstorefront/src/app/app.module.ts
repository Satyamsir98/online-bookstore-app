import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdmindashboardComponent } from './admin/admindashboard/admindashboard.component';
import { CustomerDashboardComponent } from './customer/customerdashboard/customerdashboard.component';
import { BookstoreownerdashboardComponent } from './bookstoreowner/bookstoreownerdashboard/bookstoreownerdashboard.component';
import { RegisterUserComponent } from './registeruser/registeruser.component';
import { CustomernavComponent } from './customer/customernav/customernav.component';
import { CartComponent } from './customer/cart/cart.component';
import { OrderhistoryComponent } from './customer/orderhistory/orderhistory.component';
import { BookDetailsComponent } from './customer/bookdetails/bookdetails.component';
import { BookstorenavComponent } from './bookstoreowner/bookstorenav/bookstorenav.component';
import { BookstorebookdetailsComponent } from './bookstoreowner/bookstorebookdetails/bookstorebookdetails.component';
import { AddbookComponent } from './bookstoreowner/addbook/addbook.component';
import { EditbookComponent } from './bookstoreowner/editbook/editbook.component';



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    AdmindashboardComponent,
    CustomerDashboardComponent,
    BookstoreownerdashboardComponent,
    RegisterUserComponent,
    CustomernavComponent,
    CartComponent,
    OrderhistoryComponent,
    BookDetailsComponent,
    BookstorenavComponent,
    BookstorebookdetailsComponent,
    AddbookComponent,
    EditbookComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
