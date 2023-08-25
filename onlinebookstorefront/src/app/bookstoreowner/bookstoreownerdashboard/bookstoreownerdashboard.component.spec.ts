import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookstoreownerdashboardComponent } from './bookstoreownerdashboard.component';

describe('BookstoreownerdashboardComponent', () => {
  let component: BookstoreownerdashboardComponent;
  let fixture: ComponentFixture<BookstoreownerdashboardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BookstoreownerdashboardComponent]
    });
    fixture = TestBed.createComponent(BookstoreownerdashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
