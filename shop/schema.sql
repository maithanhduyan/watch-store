
CREATE TABLE public.products (
	id serial4 NOT NULL,
	"name" varchar(64) NULL,
	barcode varchar(120) NULL,
	link varchar(1200) NULL,
	"cost" float8 NULL,
	sale_off float8 NULL,
	price float8 NULL,
	images varchar(190) NULL,
	CONSTRAINT products_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX ix_products_barcode ON public.products USING btree (barcode);
CREATE UNIQUE INDEX ix_products_name ON public.products USING btree (name);

INSERT INTO public.products (id, "name", barcode, link, "cost", sale_off, price, images) VALUES
(1, 'Apple Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-1.png'),
(2, 'Galaxy Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-2.png'),
(3, 'Motorola Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-3.png'),
(4, 'OnePlus Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-4.png'),
(5, 'Oppo Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-5.png'),
(6, 'Realme Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-6.png'),
(7, 'Redmi Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-7.png'),
(8, 'Xiaomi Watch', NULL, NULL, 25.0, 28.0, 30.0, 'static/images/showcase/showcase-8.png');