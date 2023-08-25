import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookstorenavComponent } from './bookstorenav.component';

describe('BookstorenavComponent', () => {
  let component: BookstorenavComponent;
  let fixture: ComponentFixture<BookstorenavComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BookstorenavComponent]
    });
    fixture = TestBed.createComponent(BookstorenavComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
