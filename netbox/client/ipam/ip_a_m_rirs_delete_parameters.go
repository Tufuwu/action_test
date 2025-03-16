// Code generated by go-swagger; DO NOT EDIT.

// Copyright 2018 The go-netbox Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package ipam

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/swag"

	strfmt "github.com/go-openapi/strfmt"
)

// NewIPAMRirsDeleteParams creates a new IPAMRirsDeleteParams object
// with the default values initialized.
func NewIPAMRirsDeleteParams() *IPAMRirsDeleteParams {
	var ()
	return &IPAMRirsDeleteParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewIPAMRirsDeleteParamsWithTimeout creates a new IPAMRirsDeleteParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewIPAMRirsDeleteParamsWithTimeout(timeout time.Duration) *IPAMRirsDeleteParams {
	var ()
	return &IPAMRirsDeleteParams{

		timeout: timeout,
	}
}

// NewIPAMRirsDeleteParamsWithContext creates a new IPAMRirsDeleteParams object
// with the default values initialized, and the ability to set a context for a request
func NewIPAMRirsDeleteParamsWithContext(ctx context.Context) *IPAMRirsDeleteParams {
	var ()
	return &IPAMRirsDeleteParams{

		Context: ctx,
	}
}

// NewIPAMRirsDeleteParamsWithHTTPClient creates a new IPAMRirsDeleteParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewIPAMRirsDeleteParamsWithHTTPClient(client *http.Client) *IPAMRirsDeleteParams {
	var ()
	return &IPAMRirsDeleteParams{
		HTTPClient: client,
	}
}

/*IPAMRirsDeleteParams contains all the parameters to send to the API endpoint
for the ipam rirs delete operation typically these are written to a http.Request
*/
type IPAMRirsDeleteParams struct {

	/*ID
	  A unique integer value identifying this RIR.

	*/
	ID int64

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) WithTimeout(timeout time.Duration) *IPAMRirsDeleteParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) WithContext(ctx context.Context) *IPAMRirsDeleteParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) WithHTTPClient(client *http.Client) *IPAMRirsDeleteParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) WithID(id int64) *IPAMRirsDeleteParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the ipam rirs delete params
func (o *IPAMRirsDeleteParams) SetID(id int64) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *IPAMRirsDeleteParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", swag.FormatInt64(o.ID)); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
